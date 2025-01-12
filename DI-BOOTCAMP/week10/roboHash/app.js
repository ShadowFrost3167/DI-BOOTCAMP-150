//cards

const robots = [
    {
        id: 1,
        name: 'Harry Potter',
        username: 'StarKid',
        email: 'harry@hogwarts.com',
        image: 'https://robohash.org/harrypotter?200x200'
      },
      {
        id: 2,
        name: 'Hermione Granger',
        username: 'pronouncedLeviOSa',
        email: 'hermione@hogwarts.com',
        image: 'https://robohash.org/hermionegranger?200x200'
      },
      {
        id: 3,
        name: 'Ron Weasley',
        username: 'CannonLover220',
        email: 'ron@hogwarts.com',
        image: 'https://robohash.org/ronweasley?200x200'
      },
      {
        id: 4,
        name: 'Severus Snape',
        username: 'HalfBloodPrince',
        email: 'snape@hogwarts.com',
        image: 'https://robohash.org/severussnape?200x200'
      },
    
      // Dragon Ball Characters
      {
        id: 5,
        name: 'Goku',
        username: 'MonkeyBoy',
        email: 'goku@dbz.com',
        image: 'https://robohash.org/goku?200x200'
      },
      {
        id: 6,
        name: 'Vegeta',
        username: 'ThePrince',
        email: 'vegeta@dbz.com',
        image: 'https://robohash.org/vegeta?200x200'
      },
      {
        id: 7,
        name: 'Bulma',
        username: 'HerMajesty',
        email: 'bulma@dbz.com',
        image: 'https://robohash.org/bulma?200x200'
      },
      {
        id: 8,
        name: 'Frieza',
        username: 'SupremeLeader',
        email: 'frieza@dbz.com',
        image: 'https://robohash.org/frieza?200x200'
      },
    
      // Squid Game Characters
      {
        id: 9,
        name: 'Seong Gi-hun',
        username: 'LuckyDuckling69',
        email: 'gi-hun@squidgame.com',
        image: 'https://robohash.org/seonggihun?200x200'
      },
      {
        id: 10,
        name: 'Cho Sang-woo',
        username: 'BraniacImposter',
        email: 'sang-woo@squidgame.com',
        image: 'https://robohash.org/chosangwoo?200x200'
      },
      {
        id: 11,
        name: 'Kang Sae-byeok',
        username: 'SteakGirl2021',
        email: 'sae-byeok@squidgame.com',
        image: 'https://robohash.org/kangsaebyeok?200x200'
      },
      {
        id: 12,
        name: 'Hwang In-Ho',
        username: 'FrontMan',
        email: 'frontman@squidgame.com',
        image: 'https://robohash.org/frontman?200x200'
      },
      {
        "id": 13,
        "name": "Sora",
        "username": "KeybladeMaster",
        "email": "sora@kingdomhearts.com",
        "image": "https://robohash.org/keyblademaster?200x200"
      },
      {
        "id": 14,
        "name": "Riku",
        "username": "DarknessSeeker",
        "email": "riku@kingdomhearts.com",
        "image": "https://robohash.org/darknessseeker?200x200"
      },
      {
        "id": 15,
        "name": "Kairi",
        "username": "PrincessOfHeart",
        "email": "kairi@kingdomhearts.com",
        "image": "https://robohash.org/princessofheart?200x200"
      },
      {
        "id": 16,
        "name": "Donald Duck",
        "username": "MagicalCompanion",
        "email": "donald@kingdomhearts.com",
        "image": "https://robohash.org/magicalcompanion?200x200"
      },
      {
        "id": 17,
        "name": "Goofy",
        "username": "ShieldBearer",
        "email": "goofy@kingdomhearts.com",
        "image": "https://robohash.org/shieldbearer?200x200"
      },
      {
        "id": 18,
        "name": "Aqua",
        "username": "MasterOfLand",
        "email": "aqua@kingdomhearts.com",
        "image": "https://robohash.org/masterofland?200x200"
      },
      {
        "id": 19,
        "name": "Terra",
        "username": "WarriorOfLight",
        "email": "terra@kingdomhearts.com",
        "image": "https://robohash.org/warrioroflight?200x200"
      },
      {
        "id": 20,
        "name": "Ventus",
        "username": "SwiftWind",
        "email": "ventus@kingdomhearts.com",
        "image": "https://robohash.org/swiftwind?200x200"
      },
      {
        "id": 21,
        "name": "Xehanort",
        "username": "DarknessIncarnate",
        "email": "xehanort@kingdomhearts.com",
        "image": "https://robohash.org/darknessincarnate?200x200"
      },
      {
        "id": 22,
        "name": "Mickey Mouse",
        "username": "KingOfLight",
        "email": "mickey@kingdomhearts.com",
        "image": "https://robohash.org/kingoflight?200x200"
      },
      {
        "id": 23,
        "name": "Roxas",
        "username": "TheKeybladeWielder",
        "email": "roxas@kingdomhearts.com",
        "image": "https://robohash.org/thekeybladewielder?200x200"
      },
      {
        "id": 24,
        "name": "Axel",
        "username": "FlameOfRevenge",
        "email": "axel@kingdomhearts.com",
        "image": "https://robohash.org/flameofrevenge?200x200"
      },
      {
        "id": 25,
        "name": "Saïx",
        "username": "LunarEnforcer",
        "email": "saix@kingdomhearts.com",
        "image": "https://robohash.org/lunarenforcer?200x200"
      },
      {
        "id": 26,
        "name": "Sykes",
        "username": "OrganisationXIII",
        "email": "sykes@kingdomhearts.com",
        "image": "https://robohash.org/organisationxiii?200x200"
      },
      {
        "id": 27,
        "name": "Luxord",
        "username": "GamblerOfDestiny",
        "email": "luxord@kingdomhearts.com",
        "image": "https://robohash.org/gamblerofdestiny?200x200"
      },
      {
        "id": 28,
        "name": "Marluxia",
        "username": "GracefulAssassin",
        "email": "marluxia@kingdomhearts.com",
        "image": "https://robohash.org/gracefulassassin?200x200"
      },
      {
        "id": 29,
        "name": "Larxene",
        "username": "SavageTornado",
        "email": "larxene@kingdomhearts.com",
        "image": "https://robohash.org/savagetornado?200x200"
      },
      {
        "id": 30,
        "name": "Zexion",
        "username": "SilentIntellect",
        "email": "zexion@kingdomhearts.com",
        "image": "https://robohash.org/silentintellect?200x200"
      },
      {
        "id": 31,
        "name": "Vexen",
        "username": "TheChillyResearcher",
        "email": "vexen@kingdomhearts.com",
        "image": "https://robohash.org/thechillyresearcher?200x200"
      },
      {
        "id": 32,
        "name": "Xigbar",
        "username": "TheSharpshooter",
        "email": "xigbar@kingdomhearts.com",
        "image": "https://robohash.org/thesharpshooter?200x200"
      },
      {
        "id": 33,
        "name": "Demyx",
        "username": "TheMelodiousNocturne",
        "email": "demyx@kingdomhearts.com",
        "image": "https://robohash.org/themelodiousnocturne?200x200"
      }];
const container = document.getElementById('robot-container');

robots.forEach(robot=>{
    const card = document.createElement('div');
    card.classList.add('card');
    card.innerHTML = `
    <img src ="${robot.image}" alt="${robot.name}">
    <h2>${robot.name}</h2>
    <h5>${robot.username}</h5>
    <p>${robot.email}</p>
    `;
    container.appendChild(card);
});

//search
const searchBox = document.getElementById('search-box');
const noResultsMessage = document.getElementById('no-results');
searchBox.addEventListener('input', function(){
    const searchTerm = searchBox.value.toLowerCase();
    const filteredRobots = robots.filter(robot => robot.name.toLowerCase().includes(searchTerm));

container.innerHTML = '';

if (filteredRobots.length === 0) {
    noResultsMessage.style.display = 'block'; // Show the message
} else {
    noResultsMessage.style.display = 'none';
    filteredRobots.forEach(robot=>{
    const card = document.createElement('div');
    card.classList.add('card');
    card.innerHTML = `
    <img src ="${robot.image}" alt="${robot.name}">
    <h2>${robot.name}</h2>
    <h5>${robot.username}</h5>
    <p>${robot.email}</p>
    `;
    container.appendChild(card);
});
}
});