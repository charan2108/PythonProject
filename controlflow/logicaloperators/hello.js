console.log("Just Loaded!!!");

console.log(document);

function newEl(tagName){
    const el = document.createElement(tagName);
    return el;
}

function addChildEl(parentEl, actualEl){
    parentEl.appendChild(actualEl);
}

function applyAttribute(el, attribute){
    el.setAttribute(attribute.name, attribute.value);
}

const orderedList = newEl('ol');
const firstDiv = newEl('div');
const inputEl = newEl('input');

const bodyElements = document.getElementsByTagName('body');

addChildEl(bodyElements[0], firstDiv);
addChildEl(bodyElements[0], orderedList);

let elementNames = ['div', 'img', 'h1', 'article', 'section', 'main', 'header', 'nav'];
const elementTags = [];

let task = '';
let tasks = [];

elementNames.forEach(function(elementName){
    console.log(elementName);
    // const newElement = document.createElement(elementName);
    const newElement = newEl(elementName);
    elementTags.push(newElement);
});

console.log(elementTags);


const firstH1 = newEl('h1');

firstH1.innerText = "Hello World!!";

const buttonEl = newEl('button');
buttonEl.innerText = 'Add Task'

function handleRemoveTask(ev){
    const selectedTaskNo = ev.target.getAttribute('task-no');
    console.log(typeof selectedTaskNo, "----", typeof 10);
    console.log("Button,", ev.target);
    const listItem = document.querySelector(`li[task-no="${selectedTaskNo}"]`);
    console.log("ListItem", listItem);
    orderedList.removeChild(listItem);
}

function handleAddTask(){
    tasks.push(task);
    const attribute = {
        name: 'task-no',
        value: tasks.length
    };
    const newH1 = newEl('h1');
     newH1.innerText = task;
    // firstDiv.appendChild(newH1);  
    const listItem = newEl('li');
    // listItem.setAttribute('task-no', tasks.length)
    applyAttribute(listItem, attribute);

    addChildEl(listItem, newH1);



    const deleteTaskButton = newEl('button');
    deleteTaskButton.innerText = 'Remove';
    applyAttribute(deleteTaskButton, attribute);
    deleteTaskButton.addEventListener('click', handleRemoveTask)
    addChildEl(listItem, deleteTaskButton);

    addChildEl(orderedList, listItem);
    inputEl.value = '';
}


buttonEl.addEventListener('click', handleAddTask);



inputEl.addEventListener('change', function(ev){
        console.log('From change Event Listener', ev);
        task = ev.target.value;
});



const brEl = newEl('br');
const brEl1 = newEl('br');

addChildEl(firstDiv,firstH1);
addChildEl(firstDiv,inputEl);
addChildEl(firstDiv,brEl);
addChildEl(firstDiv,brEl1);
addChildEl(firstDiv,buttonEl);
console.log("This is DIV",firstDiv);


console.log("Just Loaded!!!");

console.log(document);

function newEl(tagName){
    const el = document.createElement(tagName);
    return el;
}

function addChildEl(parentEl, actualEl){
    parentEl.appendChild(actualEl);
}

function applyAttribute(el, attribute){
    el.setAttribute(attribute.name, attribute.value);
}

const orderedList = newEl('ol');
const firstDiv = newEl('div');
const inputEl = newEl('input');

const bodyElements = document.getElementsByTagName('body');

addChildEl(bodyElements[0], firstDiv);
addChildEl(bodyElements[0], orderedList);

let elementNames = ['div', 'img', 'h1', 'article', 'section', 'main', 'header', 'nav'];
const elementTags = [];

let task = '';
let tasks = [];

elementNames.forEach(function(elementName){
    console.log(elementName);
    // const newElement = document.createElement(elementName);
    const newElement = newEl(elementName);
    elementTags.push(newElement);
});

console.log(elementTags);


const firstH1 = newEl('h1');

firstH1.innerText = "Hello World!!";

const buttonEl = newEl('button');
buttonEl.innerText = 'Add Task'

function handleRemoveTask(ev){
    const selectedTaskNo = ev.target.getAttribute('task-no');
    console.log(typeof selectedTaskNo, "----", typeof 10);
    console.log("Button,", ev.target);
    const listItem = document.querySelector(`li[task-no="${selectedTaskNo}"]`);
    console.log("ListItem", listItem);
    orderedList.removeChild(listItem);
}

function handleAddTask(){
    tasks.push(task);
    const attribute = {
        name: 'task-no',
        value: tasks.length
    };
    const newH1 = newEl('h1');
     newH1.innerText = task;
    // firstDiv.appendChild(newH1);  
    const listItem = newEl('li');
    // listItem.setAttribute('task-no', tasks.length)
    applyAttribute(listItem, attribute);

    addChildEl(listItem, newH1);



    const deleteTaskButton = newEl('button');
    deleteTaskButton.innerText = 'Remove';
    applyAttribute(deleteTaskButton, attribute);
    deleteTaskButton.addEventListener('click', handleRemoveTask)
    addChildEl(listItem, deleteTaskButton);

    addChildEl(orderedList, listItem);
    inputEl.value = '';
}


buttonEl.addEventListener('click', handleAddTask);



inputEl.addEventListener('change', function(ev){
        console.log('From change Event Listener', ev);
        task = ev.target.value;
});



const brEl = newEl('br');
const brEl1 = newEl('br');

addChildEl(firstDiv,firstH1);
addChildEl(firstDiv,inputEl);
addChildEl(firstDiv,brEl);
addChildEl(firstDiv,brEl1);
addChildEl(firstDiv,buttonEl);
console.log("This is DIV",firstDiv);

