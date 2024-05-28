export default function getStudentsByLocation(list, city) {
  return list.filter((students) => students.location === city);
}
