"use strict"

//Get words from user
function getWords()
{	
	let words = [];
	words.push("This",);
	let count = 0;
	while(count < 5)
	{
		let thisWord = prompt("Enter a word");
		words.push(thisWord);
		count++;
	}
	console.log(words);
}


//Changing text of the #output element
function changeText(newText)
{
	let theElement = document.getElementById('output');
	
	let myPageText = (!newText) ? promptUser("Please enter some text") : newText;
	theElement.innerHTML = myPageText;
}

function promptUser(theQuestion)
{
	return prompt(theQuestion);
}

function getSomeNumbers()
{
	let count = prompt("Enter a number");
	let numbers = "";
	if(isNaN(count))
	{
		count = prompt("I need a real number");
		getSomeNumbers();
	}
	else
	{
		for(let i=10; i>count; i--)
		{
			let newNumber = Math.floor(Math.random() * 101);
			numbers += newNumber;
			numbers += "<br>";
		}
		
		/* let n = 0;
		while(n<count)
		{
			let newNumber = Math.floor(Math.random() * 101);
			numbers += newNumber;
			numbers += "<br>";
			n++;
		} */
		document.getElementById("myNumbers",).innerHTML = numbers;
	}
}


//Setting the date text in the html
function setDateText()
{
	let today = new Date();
	let shortDate = new Date();
	let yesterday = new Date(2019,9,27);
	let stringDate = new Date("February 3, 2018 3:15:28");
	let month = today.getMonth()+1;
	let day = today.getDate();
	let year = today.getFullYear();
	let fullDate = month + "/" + day + "/" + year;
	document.getElementById("month").innerHTML += month;
	document.getElementById("day").innerHTML += day;
	document.getElementById("year").innerHTML += year;
	document.getElementById("fullDate").innerHTML += fullDate;
}

//getWords();

function compareValues()
{
	let val_one = 50;
	let val_two = Math.floor(Math.random() * 101);
	let val_three = "50";
	let val_four = 50;
	
	if(val_one == val_three)
	{
		
	}
	else
	{
		alert("NOT EQUAL");
	}
	
	
	
	
	
	/* if(val_one == val_three)
	{
		alert("Values one and three Are equal");
	}
	else if(val_one === val_four)
	{
		alert("Values 1 and 4 are the same");
	}
	else
	{
		alert("Values Are Equal");
	}
	
	
	if(val_one > val_two)
	{
		alert("Value One is Greater");
	}
	else if(val_one < val_two)
	{
		alert("Value Two is Greater");
	}
	else if(val_one === val_two)
	{
		alert("Value One and Value Two are Equal");
	}
	else
	{
		alert("Something went wrong");
	} */
}







function infinite_loop()
{	
	let count = 0;
	while(count >= 0)
	{
		//alert(count);
		console.log(count);
		count++;
	}
}


function getThis()
{
	for (var i = 0; i < ratingsCount; i++) 
	{
	   ratingsSum += ratings[i];
	}
}

//let myInterval = setInterval(changeCards, 1000);

let myInterval = "";

function setMyInterval()
{
	myInterval = setInterval(changeCards, 1000);
}

function clearMyInterval()
{
	clearInterval(myInterval);
}

function changeCards()
{
	//let imgHTML = "<img src='cards/";
	let randomNum = Math.floor(Math.random()*(cards.length-1));
	//imgHTML += cards[randomNum];
	//imgHTML += ".jpg' alt='" + cards[randomNum] + "' />";
	//document.getElementById("images").innerHTML = imgHTML;
	let newImage = "cards/" + cards[randomNum] + ".JPG";
	let randomPos = Math.floor(Math.random()*100);
	document.getElementById("imageToChange").src = newImage;
	document.getElementById("imageToChange").style.display = "block";
	
	document.getElementById("imageToChange").style.left = randomPos+"%";
	document.getElementById("imageToChange").style.top = randomPos+"%";
}

let cards = [
	"2Clubs",
	"2Diamonds",
	"2Hearts",
	"2Spades",
	"3Clubs",
	"3Diamonds",
	"3Hearts",
	"3Spades",
	"4Clubs",
	"4Diamonds",
	"4Hearts",
	"4Spades",
	"5Clubs",
	"5Diamonds",
	"5Hearts",
	"5Spades",
	"6Clubs",
	"6Diamonds",
	"6Hearts",
	"6Spades",
	"7Clubs",
	"7Diamonds",
	"7Hearts",
	"7Spades",
	"8Clubs",
	"8Diamonds",
	"8Hearts",
	"8Spades",
	"9Clubs",
	"9Diamonds",
	"9Hearts",
	"9Spades",
	"10Clubs",
	"10Diamonds",
	"10Hearts",
	"10Spades",
	"JClubs",
	"JDiamonds",
	"JHearts",
	"JSpades",
	"QClubs",
	"QDiamonds",
	"QHearts",
	"QSpades",
	"KClubs",
	"KDiamonds",
	"KHearts",
	"KSpades",
	"AClubs",
	"ADiamonds",
	"AHearts",
	"ASpades"
];

function show_hide_buttons()
{
	let buttonDiv = document.getElementById("buttons");
	//if(buttonDiv.style.display == "none")
	if(buttonDiv.style.visibility == "hidden")
	{
		//buttonDiv.style.display = 'block';
		buttonDiv.style.visibility = 'visible';
	}
	else
	{
		//buttonDiv.style.display = 'none';
		buttonDiv.style.visibility = 'hidden';
	}
}
 










































