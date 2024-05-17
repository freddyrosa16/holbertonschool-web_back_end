function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve('true');
      reject(new Error('An error occurred'));
    });
  });
}
export default getResponseFromAPI;
