/* Nos dan steps como el número de peldaños de la escalera y el número máximo de peldaños maxJump que un elfo puede saltar en un solo salto.

Tu tarea es ayudar a los elfos a encontrar todas las posibles secuencias de saltos que pueden hacer para subir la escalera, ordenadas de menos a más. Teniendo en cuenta que los elfos pueden saltar como máximo maxJump peldaños en un solo salto (pero pueden saltar menos peldaños si así lo desean).

Por ejemplo, si hay una escalera de steps = 4 y maxJump = 2 es el número máximo de peldaños que un elfo puede saltar en un solo salto, entonces hay cinco secuencias de saltos posibles:

• [1, 1, 1, 1] (salta 1 peldaño 4 veces)
• [1, 1, 2] (salta 1 peldaño 2 veces y luego 2 peldaños)
• [1, 2, 1] (salta 1 peldaño, luego 2 peldaños y luego 1 peldaño)
• [2, 1, 1] (salta 2 peldaños, luego 1 peldaño y luego 1 peldaño)
• [2, 2] (salta 2 peldaños 2 veces) */
function getStaircasePaths(steps: number, maxJump: number): number[][] {
  const paths: number[][] = [];

  function getPaths(
    remainingSteps: number,
    currentPath: number[]
  ): void {
    if (remainingSteps === 0) {
      paths.push([...currentPath]);
      return;
    }

    const maxJumpSize = Math.min(maxJump, remainingSteps);
    for (let jump = 1; jump <= maxJumpSize; jump++) {
      getPaths(remainingSteps - jump, [...currentPath, jump]);
    }
  }

  getPaths(steps, []);
  return paths;
}

getStaircasePaths(4, 2); // [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2]]
getStaircasePaths(3, 3); // [[1, 1, 1], [1, 2], [2, 1], [3]]