export default function getStudentIdsSum(list) {
  const num = list.map((id) => id.id);
  return num.reduce((num1, num2) => num1 + num2, 0);
}
