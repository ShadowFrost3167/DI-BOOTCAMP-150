

function checkAnagrams(str1, str2) {
    
    str1 = str1.replace(/\s+/g, '').toLowerCase();
    str2 = str2.replace(/\s+/g, '').toLowerCase();

    // If the lengths !==, can't be anagrams
    if (str1.length !== str2.length) {
        return false;

    }

    // Sort strings and compare
    return str1.split('').sort().join('') === str2.split('').sort().join('');
}


//button and add event listener

const annnagram = document.getElementById('anagrammy');
const notAnnnagram = document.getElementById('notAnagrammy');
const duplicateError = document.getElementById('duplicateError');

document.getElementById('checkButton').addEventListener('click', function(){

    const str1 = document.querySelector('#stringOne input').value;
    const str2 = document.querySelector('#stringTwo input').value;

    //check duplicates
    if (str1.trim().toLowerCase() === str2.trim().toLowerCase()){

        duplicateError.style.display = 'block';
        annnagram.style.display = 'none';
        notAnnnagram.style.display = 'none';

        //duplicate error fadeaway
        setTimeout(function () {
            duplicateError.classList.add('fade-out');
        }, 1000);

        // Hide the message completely after it fades out
        setTimeout(function () {
            duplicateError.style.display = 'none';
            duplicateError.classList.remove('fade-out'); // Reset the opacity for next use
        }, 3000); // 1s for fade out + 2s wait = 3s in total
    } else{
        duplicateError.style.display = 'none';
    }

    const result = checkAnagrams(str1, str2);

    annnagram.style.display = 'none';
    notAnnnagram.style.display = 'none';

    if (result){
        annnagram.style.display = 'block';

        
    }
    else{
        notAnnnagram.style.display = 'block';
    }
});