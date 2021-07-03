function powerset(s) {
  // base case
  if (s.length == 0) return [[]];
  // recursive step
  const without_first = powerset(s.slice(1));
  // subsets with first elem
  const with_first = without_first.map((el) => [s[0]].concat(el));
  // return
  return with_first.concat(without_first);
}
console.log(powerset(["A", "B", "C", "D"]));
