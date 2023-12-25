/* El problema es que el formato de los árboles ha cambiado. Es un array de números… ¡pero debería ser un objeto! Por ejemplo el árbol: [3, 1, 0, 8, 12, null, 1] se ve así:
//        3
//      /   \
//     1     0
//    / \     \
//   8  12     1
Lo que necesitamos es transformar el array en un objeto donde cada nodo del árbol tiene las propiedades value, left y right. Si un nodo no tiene valor, se representa con null. Por lo tanto, si un nodo tiene valor null, no tendrá hijos. El nodo raíz se encuentra en el índice 0 del array. Existe una relación entre el índice de un nodo y el índice de sus hijos.*/

interface TreeNode {
  value: number | null;
  left: TreeNode | null;
  right: TreeNode | null;
}

function transformTree(tree: number[], index: number): TreeNode | null{
  if(index >= tree.length || tree[index] === null) return null;

  const treeNode: TreeNode = {
    value: tree[index] as number,
    left: transformTree(tree, 2 * index + 1),
    right: transformTree(tree, 2 * index + 2),
  }

  return treeNode;
}