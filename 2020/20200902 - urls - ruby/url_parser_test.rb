# Please, stop your cursor here >>>
# Write the code here

# Exemplos:
#
# Entrada: http://www.google.com/mail?user=fulano&senha=123
#    Saída:
#    protocolo: http
#    host: www
#    domínio: google.com
#    path: mail
#    parâmetros: user=fulano
# Entrada: ssh://fulano%senha@git.com/
#    Saída:
#    protocolo: ssh
#    usuário: fulano
#    senha: senha
#    dominio: git.com

def url_parser_ssh(link)
  parsed_url = { protocolo: 'ssh'}
  usuario, resto = link.split('%')
  parsed_url[:usuario] = usuario
  senha, resto = resto.split('@')
  parsed_url[:senha] = senha
  dominio, resto = resto.split('/')
  parsed_url[:dominio] = dominio
  parsed_url
end

def url_parser_http(link)
  parsed_url = { protocolo: 'http'}
  host, *resto = link.split('.')  # host = 'www', resto = ['google', 'com/path?user=fulano']
  
  parsed_url[:host] = host
  resto = resto.join('.')
  dominio, resto = resto.split('/')
  parsed_url[:dominio] = dominio
  path, resto = resto.split('?')
  parsed_url[:path] = path

  # resto = user=fulano&senha=123
  parsed_url[:parametros] = {}

  parsed_url
end

def url_parser(link)
  protocolo, resto = link.split('://')

  if protocolo == 'ssh'
    return url_parser_ssh(resto)
  end

  if protocolo == 'http'
    return url_parser_http(resto)
  end
  
  raise 'Não é url'
end

require 'minitest/autorun'

class TestHTTP < MiniTest::Unit::TestCase
  def test_url_parser_parametros
    assert_equal({user: 'fulano', senha: '123'}, url_parser('http://www.google.com/mail?user=fulano&senha=123')[:parametros])
  end 

  def test_url_parser_path
    assert_equal 'mail', url_parser('http://www.google.com/mail?user=fulano')[:path]
  end 

  def test_url_parser_dominio
    assert_equal 'google.com', url_parser('http://www.google.com/mail?user=fulano')[:dominio]
  end 

  def test_url_parser_host
    assert_equal 'www', url_parser('http://www.google.com/mail?user=fulano')[:host]
  end
  
  def test_url_parser_protocolo
    assert_equal 'http', url_parser('http://www.google.com/mail?user=fulano')[:protocolo]
  end

  def test_url_parser_invalido
    assert_raises { url_parser('não é url') }
  end
end

class TestSSH < MiniTest::Unit::TestCase
  def test_url_parser_dominio
    assert_equal 'git.com', url_parser('ssh://fulano%senha@git.com/')[:dominio]
  end

  def test_url_parser_senha
    assert_equal 'senha', url_parser('ssh://fulano%senha@git.com/')[:senha]
  end

  def test_url_parser_usuario
    assert_equal 'fulano', url_parser('ssh://fulano%senha@git.com/')[:usuario]
  end
  
  def test_url_parser_protocolo
    assert_equal 'ssh', url_parser('ssh://fulano%senha@git.com/')[:protocolo]
  end

  def test_url_parser_invalido
    assert_raises { url_parser('não é url') }
  end
end

