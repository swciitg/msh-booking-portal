const rollnoInput = document.querySelector('input[name=roll_number]');
const slugInput = document.querySelector('input[name=slug]');

const slugify = (val) => {

    return val.toString()

};

rollnoInput.addEventListener("keyup", myScript);

function myScript(){
    slugInput.setAttribute("value", slugify(rollnoInput.value));
}