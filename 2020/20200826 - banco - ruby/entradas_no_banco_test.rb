# Deixe seu cursor aqui >>  
# http://dojopuzzles.com/problemas/exibe/entradas-no-banco/
# Write the code here

=begin
O gerente do banco precisa saber quantas pessoas entraram no 
banco no horário de expediente, para isso ele solicitou 
que você faça um programa que verifique se o registro de 
entrada é válido e se a hora se encontra dentro do intervalo 
de funcionamento do banco, das 10:00:00 até as 16:00:00.
=end

# [YYYY-mm-dd H:i:s] - Abertura da Porta OK

require 'minitest/autorun'

# hora =~ /\d\d:\d\d:\d\d/

## ['data', 'hora', '-', 'Abertura', 'da', 'porta'....]

INICIO = 10
FIM = 16

def entrada_no_horario_comercial(linha_do_log)
  hora = linha_do_log[11..12].to_i

  (INICIO...FIM).include? hora  
end

def contar(log)
  contador = 0
  log.each do |linha|
    contador +=1 if entrada_no_horario_comercial(linha)
  end
  contador
end

class TestDojoCode < MiniTest::Unit::TestCase
  def test_contar_retorna_2_com_log_4()
    assert_equal 2, contar([
      '2008-02-07 09:10:10 - Abertura da Porta OK',
      '2008-02-07 11:10:10 - Abertura da Porta OK',
      '2008-02-07 11:10:10 - Abertura da Porta OK',
      '2008-02-07 16:10:10 - Abertura da Porta OK'
    ])
  end

  def test_contar_retorna_2_com_log_3()
    assert_equal 2, contar([
      '2008-02-07 09:10:10 - Abertura da Porta OK',
      '2008-02-07 11:10:10 - Abertura da Porta OK',
      '2008-02-07 11:10:10 - Abertura da Porta OK'
    ])
  end

  def test_contar()
    assert_equal 1, contar(['2008-02-07 11:10:10 - Abertura da Porta OK'])
  end

  def test_contar_retorna_2()
    assert_equal 2, contar([
      '2008-02-07 11:10:10 - Abertura da Porta OK',
      '2008-02-07 11:10:10 - Abertura da Porta OK'
    ])
  end

  def test_entrada_do_log_no_horario_comercial()
    assert_equal entrada_no_horario_comercial('2008-02-07 11:10:10 - Abertura da Porta OK'), true
  end

  def test_entrada_do_log_fora_do_horario_comercial()
    assert_equal entrada_no_horario_comercial('2008-02-07 09:10:10 - Abertura da Porta OK'), false
  end

  def test_entrada_do_log_9_11_fora_do_horario_comercial()
    assert_equal entrada_no_horario_comercial('2008-02-07 09:11:10 - Abertura da Porta OK'), false
  end

  def test_entrada_do_log_10_00_dentro_do_horario_comercial()
    assert_equal entrada_no_horario_comercial('2008-02-07 10:00:00 - Abertura da Porta OK'), true
  end

  def test_entrada_do_log_16_00_fora_do_horario_comercial()
    assert_equal entrada_no_horario_comercial('2008-02-07 16:00:00 - Abertura da Porta OK'), false
  end

  def test_entrada_do_log_18_11_fora_do_horario_comercial()
    assert_equal entrada_no_horario_comercial('2008-02-07 18:11:10 - Abertura da Porta OK'), false
  end
end