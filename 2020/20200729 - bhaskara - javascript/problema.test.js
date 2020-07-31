// (-b +- sqrt(b² - 4ac)) / 2a
// ax^2 + bx + c = 0
// x^2 - 10x + 24 = 0 raizes 4 e 6
// Posicionem o cursor aqui de quem não estiver como piloto ou co-piloto ->:

const menos = (a, b=0) => a * -1

// function menos(a){  
//   return a * -1
// }
function raizQuadrada(valor){
  // this.a = 1;
  // console.log(this.a)
  // function interno () {
    // console.log('interno')
    // console.log(this.a)
    // console.log('fim')
  // }
  // interno()
  return Math.sqrt(valor)
}

function bhaskara(a, b, c) {
  const delta = Math.pow(b, 2) -4 * a * c
  const raiz1 = (menos( b ) + raizQuadrada( delta )) / (2 * a) 
  const raiz2 = (menos(b) - raizQuadrada(delta)) / (2 * a)
  return [raiz1 || 0, raiz2 || 0]
}

// Nossos testes aqui em baixo:
test('x^2 - 10x + 24 = 0', () => {
  expect(bhaskara(1, -10, 24)).toStrictEqual([6, 4]);
});

test('x^2 = 0', () => {
  expect(bhaskara(1, 0, 0)).toStrictEqual([0, 0]);
});

test('5x^2 = 0', () => {
  expect(bhaskara(5, 0, 0)).toStrictEqual([0, 0]);
});

test('10x^2 = 0', () => {
  expect(bhaskara(10, 0, 0)).toStrictEqual([0, 0]);
});

test('x^2 - 25 = 0', () => {
  expect(bhaskara(1, 0, -25)).toStrictEqual([5, -5]);
});

test('x^2 - 36 = 0', () => {
  expect(bhaskara(1, 0, -36)).toStrictEqual([6, -6]);
});
