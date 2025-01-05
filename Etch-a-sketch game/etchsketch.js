document.addEventListener("DOMContentLoaded", function(){
    const canvas = document.getElementById('etchASketchCanvas');
    const ctx = canvas.getContext('2d');

// Initial setup
let x = canvas.width / 2;
let y = canvas.height / 2;
let penX = x; // Added variable to track pen's x coordinate
let penY = y; // Added variable to track pen's y coordinate
let penSize = 5;
let penColor = "black";
let direction = 0; // 0: up, 1: down, 2: left, 3: right
let shapeIndex = 0;
let turtleSpeed=10;
// Function to draw
function draw() {
    ctx.beginPath();
    ctx.moveTo(penX, penY);
    if (direction === 0) {
        penY -=turtleSpeed;
        drawTurtle();
        console.log(`${penX},${penY}`)
    } else if (direction === 1) {
        penY +=turtleSpeed;
        drawTurtle();
        console.log(`${penX},${penY}`)
    } else if (direction === 2) {
        penX -=turtleSpeed;
        drawTurtle();
        console.log(`${penX},${penY}`)
    } else if (direction === 3) {
        penX +=turtleSpeed;
        drawTurtle();
        console.log(`${penX},${penY}`)
    }
    ctx.lineTo(penX, penY);
    ctx.lineWidth = penSize;
    ctx.strokeStyle = penColor;
    ctx.stroke();
    ctx.closePath();
}
let turtle=new Image();
turtle.src="gun.gif";

    function drawTurtle() {
        if (!animationActive) return;
        penX += turtleSpeed;
        penY += turtleSpeed;
        if (penX + 50 > canvas.width || penX < 0 || penY + 50 > canvas.height || penY < 0) {
            console.log("touvched");// Exit the function to prevent further drawing
            return; 
        }
        c.drawImage(fishImage, penX, penY, 50, 50);
        }
// Functions to handle key events
function handleKeyEvents(event) {
    canvas.innerHTML="<img src='gun.gif'>";
    switch (event.key) {
        case 'w':
            direction = 0;
            draw();
            break;
        case 's':
            direction = 1;
            draw();
            break;
        case 'a':
            direction = 2;
            draw();
            break;
        case 'd':
            direction = 3;
            draw();
            break;
        case 'c':
            clearCanvas();
            break;
        case 'f':
            drawCircle();
            break;
        case ' ':
            changeColor();
            break;
        case 'k':
            increasePenWidth();
            break;
        case 'o':
            decreasePenWidth();
            break;
        case 'y':
            changeShape();
            break;
        case 'x':
            originalShape();
            break;
    }
}

// Function to clear canvas
function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}

// Function to draw a circle
function drawCircle() {
    ctx.beginPath();
    ctx.arc(penX, penY, 25, 0, Math.PI * 2);
    ctx.fillStyle = penColor;
    ctx.fill();
    ctx.closePath();
}

// Function to change pen color
function changeColor() {
    const colors = ['black', 'white', 'red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink', 'brown'];
    penColor = colors[Math.floor(Math.random() * colors.length)];
}

// Function to increase pen width
function increasePenWidth() {
    penSize += 5;
}

// Function to decrease pen width
function decreasePenWidth() {
    penSize -= 5;
    if (penSize < 1) {
        penSize = 1;
    }
}

// Function to change shape
function changeShape() {
    const shapes = ['arrow', 'circle', 'square', 'triangle', 'classic'];
    shapeIndex = (shapeIndex + 1) % shapes.length;
    canvas.style.cursor = "url('" + shapes[shapeIndex] + ".png'), auto";
}

// Function to revert to original shape
function originalShape() {
    canvas.style.cursor = "auto";
}





// Event listener for keydown events
document.addEventListener('keydown', handleKeyEvents);

})