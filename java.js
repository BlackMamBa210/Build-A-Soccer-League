console.log("Start program");
alert("Welcome to the Story Maker");
console.log("Take info for story");
// First part of the story.
var charName = prompt("What is your full name?");
var charNickname = prompt("What do you prefer to be called?");
var birthCity = prompt("Where are you from?");
var adjective1 = prompt("Please enter an adjective.");
var adjective2 = prompt("Please enter another adjective.");
var adjective3 = prompt("Please enter a final adjective.");
var verb1 = prompt("Please enter a verb.");
var verb2 = prompt("Please enter another verb.");
var message = ("There ") + ("once ") + ("was ") + ("a ") + ("beautiful ") + ("girl ") + ("called ") + charName + (", ") + ("but ") + ("everyone ") + ("called ") + ("her ") + charNickname + (" she ") + ("came ") + ("from ") + ("a ") + ("place ") + ("faraway ") + ("called ") + birthCity + (". ") + charNickname + ("'s ") + ("favourite ") + ("thing ") + ("to ") + ("do ") + ("was ") + verb1 + (" while ") + ("farting ") + ("really ") + ("loudly ") + ("or ") + ("doing ") + ("a ") + ("poo. ") + ("One ") + ("day ") + ("after ") + ("a ") + adjective2 + (" poo, ") + charNickname + (" decided ") + ("to ") + ("move ") + ("to ") + ("Liverpool ") + ("where ") + ("she ") + ("met ") + ("a ") + adjective1 + ", " + adjective3 + (" fella ") + ("called ") + ("Dean, ") + ("who ") + ("loved ") + ("her ") + ("more ") + ("than ") + ("anything ") + ("and") + ("they ") + ("lived ") + ("happily ") + ("ever ") + ("after.");

// **** EXAMPLE OF STORY *****
// There once was a beautiful girl called Codruta, but everyone called her Cody she came from a place faraway called Romania. Cody's favourite thing to do was "swimming" while farting really loudly or doing a poo. On one day after a "hard" poo, Cody decided to move to Liverpool where she met a "smart", "handsome" fella called Dean, who loved her more than anything and they lived happily ever after.

//Start of document write
console.log("Execute program.");

document.write(message);

console.log("End of story");

alert("The End. Hope your enjoyed your story");

console.log("End program.");
//---------------------------------------------------------------------------