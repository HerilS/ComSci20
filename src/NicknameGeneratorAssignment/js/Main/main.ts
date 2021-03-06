const nameInput = document.getElementById("nameInput") as HTMLInputElement;
const randomNickBtn = document.getElementById("randomNickBtn");
const allNickBtn = document.getElementById("allNickBtn");
const responseSection = document.getElementById("responseSection");

// all possible nicknames that can be shown
const allNicknames = [
  `"Crusher"`,
  `"The Scientist"`,
  `"The Madman"`,
  `"The Coder"`,
  `"The Jester"`,
  `"The Sloth"`,
  `"Quick-Silver"`,
  `"Retro"`,
];

const getRandomNick = () => {
  // split name string into [firstName, lastName]
  const inputValArr = nameInput.value.split(" ");

  // get random index position in allNicknames array
  const randIdx = Math.round(Math.random() * (allNicknames.length - 1));

  /* add nickname to the middle of the array
   * (e.g. [firstName, lastName] -> [firstName, nick, lastName])
   * */
  inputValArr.splice(1, 0, allNicknames[randIdx]);

  // join array back into string with spaces in between each word
  responseSection.innerHTML = `${inputValArr.join(" ")}`;
};

const getAllNicks = () => {
  // split name string into [firstName, lastName]
  const inputValArr = nameInput.value.split(" ");

  // innerHTML of responseSection
  let htmlStr = ``;

  // iterate through all nicknames and add to responseStr
  for (let i = 0; i < allNicknames.length; i++) {
    htmlStr += `<div>${inputValArr[0]} ${allNicknames[i]} ${inputValArr[1]}</div>`;
  }

  responseSection.innerHTML = htmlStr;
};

randomNickBtn.addEventListener("click", getRandomNick);
allNickBtn.addEventListener("click", getAllNicks);
