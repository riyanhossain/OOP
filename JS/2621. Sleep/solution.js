/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
  return new Promise((resolve, reject) => {
    if (!millis) {
      reject("rejected");
    }
    setTimeout(() => {
      resolve("resolved");
    }, millis);
  });
}

let t = Date.now()
sleep(100).then(() => console.log(Date.now() - t)) // 100

