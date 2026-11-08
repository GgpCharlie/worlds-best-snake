// Wooden supply crates for Battle Mini 3D — place a few around the map.
// Same blocky style as the rest of the game's art. Loaded before the game script.
function makeCrate() {
  const g = new THREE.Group();
  const wood = new THREE.MeshLambertMaterial({ color: 0x8a5a2b });
  const dark = new THREE.MeshLambertMaterial({ color: 0x5f3d1c });
  const box = new THREE.Mesh(new THREE.BoxGeometry(1.6, 1.6, 1.6), wood);
  box.position.y = 0.8;
  g.add(box);
  for (const s of [-1, 1]) {
    const bar1 = new THREE.Mesh(new THREE.BoxGeometry(1.66, 0.22, 1.66), dark);
    bar1.position.y = 0.35 + (s + 1) * 0.55;
    g.add(bar1);
    const bar2 = new THREE.Mesh(new THREE.BoxGeometry(0.22, 1.66, 1.66), dark);
    bar2.position.set(s * 0.55, 0.8, 0);
    g.add(bar2);
    const bar3 = new THREE.Mesh(new THREE.BoxGeometry(1.66, 1.66, 0.22), dark);
    bar3.position.set(0, 0.8, s * 0.55);
    g.add(bar3);
  }
  const lid = new THREE.Mesh(new THREE.BoxGeometry(1.7, 0.12, 1.7), dark);
  lid.position.y = 1.62;
  g.add(lid);
  g.traverse(o => { if (o.isMesh) o.userData.crate = true; });
  return g;
}
