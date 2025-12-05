window.addEventListener("load", function () {

    ejemplo();
});

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function ejemplo() {
  const InicioTiempo = performance.now();

  console.log("Inicia pausa...");
  await sleep(2000); // pausa de 2 segundos

  const FinTiempo = performance.now();

  console.log("Fin de la pausa");
  console.log("Tiempo total: " + (FinTiempo - InicioTiempo) + " ms");
}

