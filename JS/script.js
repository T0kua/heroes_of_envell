//--------------------переменные--------------------------------------//
var canvas = document.getElementById('canvas')
var set    = canvas.getContext('2d')
var x = 30 // x утюга
var y = 240 // y утюга
var rx = 760 // x припятствия
var ry = ran(0,411) //рандомайзер положений припятствия
console.log(rx) //тест рандомайзера
var img = new Image() //локация
img.src = 'https://i.pinimg.com/originals/e9/2f/03/e92f03ace41d591e3c3f7454105dcffb.jpg' //ссылкка на локацию
var play1 = new Image() //переменная утюг
play1.src = 'sprite/утюг2.png' //ссылка на утюг
var agry = new Image() // вражеский утюг
agry.src = 'sprite/злойутюг.png' //ссылка на вражеский утюг
var xp = 30 //жизни
var score = 0 //очки
set.font = '30px segoe print' //шрифт
var final = false //правило игры отвечающиеся за финал
//
var screen = new Image() // эмблемы игроков
screen.src = 'db_art/screen.png' //ссылка
var mp3 = 1 //так надо
var boss = new Image()
boss.src = 'sprite/boss.png'
var locationX = 0
var bos = {
 x : 0,
 y : 240,
 xp : 350
}
//
//--------------------------------игра--------------------------------//
function game(){
 if ( bos.xp <= 0){
  final = true
 }
 set.clearRect(0,0,canvas.width,canvas.height)
 locationX -= 0.1
 if (locationX <  canvas.width - img.width){//-700
 	locationX = 0
 }
 if (score <= 30 ){ //начало части кода отвечающей за локации
 	img.src = 'https://i.pinimg.com/originals/e9/2f/03/e92f03ace41d591e3c3f7454105dcffb.jpg'
 }
 if(score > 30){
 	img.src = 'location/location1.jpg'
 }
 if (score > 56){
 	img.src = 'location/location2.jpg'
 }
 if (score > 87){
 	img.src = 'location/location3.jpg'
 }
 if (score > 120){
  img.src = 'location/location5.jpg'
  if (mp3 == 1){
   $('#misik').attr('src','track/track2.mp3')
   mp3 = 2
  }
 }
 if (score > 160){
  set.fillStyle = 'black'
  img.src = 'location/location6.jpg'
 }
 if (score > 200){
  img.src = 'location/location4.jpg'
 }
 if (score > 300){
  img.src = 'location/location_boss.jpg'
  rx = 1000
  x = 660
  locationX = 0
 }
 if (final == true){
  x = 30
  img.src = 'location/final.jpg'
 }
  //конец части отвечающей за локаци
 set.drawImage(img,locationX,0)
 if (rx <= -100){
	ry = ran(0,411) //рандомайзер положений 
	rx = 760
 }
 if (xp <= 0){
  alert('game over')
  xp = 30
  score = 0
  $('#misik').attr('src','track/track1.mp3')
  locationX  = 0
 }
};

$('#down').click(function(){
  if (y < 385){
	y += 10
  }
})
$('#up').click(function(){
 if (y > 0){
	y -= 10
 }
})
function ran(min,max){return(Math.floor(Math.random() * (max - min)) + min);}
document.addEventListener('keydown',function(e){ //управление
 if (y > 0){
  if (e.which === 38){ //вверх
	y -= 10
  }
 }
 if (y < 385){
  if (e.which === 40){ //вниз
	y += 10
  }
 }
 if (y > 0){
  if (e.which === 87){ //вверх
	y -= 10
  }
 }
 if (y < 385){
  if (e.which === 83){ //вниз
	y += 10
  }
 }
 if (e.which === 32){
  bos.xp -= 10
 }
})
boss.onload = function(){
setInterval(function(){ //анимация на экране
game() //функция игры
if (score >= 300){
  set.drawImage(boss,bos.x,bos.y,300,300)
  set.fillStyle = 'black'
  set.fillRect(200,30,350,30)
  set.fillStyle = 'red'
  set.fillRect(200,30,bos.xp,30)
  set.fillStyle = 'white'
  set.font = '30px Small Fonts'
  set.fillText('HECATONCHEIR',240,55)
  // boss battle
}
if (final == true){
  set.fillStyle = 'black'
  set.font = '30px segoe print'
  set.fillText('художники :',90,30)
  set.fillText('Стёпа Белохвостов',10,70)
  set.fillText('Женя Сузенко',10,100)
  set.fillText('программисты :',460,70)
  set.fillText('Филипп Новиков',465,110)
  set.fillText('Тестеры:',270,370)
  set.fillText('Ваня Курапикова',435,380)
  set.fillText('Илья Липецкий',430,410)
  set.fillText('Вова Брежнев',430,440)
  set.fillText('Валентина Новикова',430,470)
  set.fillText('please press "F5" ',260,240)
  score = - 1
}
set.fillStyle = 'black' 
play1.src = 'sprite/утюг2.png'
set.drawImage(play1,x,y) // рисовка утюга
if (score > 120){
  set.fillStyle = 'purple'
}
if (score > 170){
  set.fillStyle = 'black'
}
set.fillRect(rx,ry,100,170)//рисовка "припятствия"
set.fillStyle = 'red'
 // и это
set.fillRect(36,468,xp,8)
set.fillRect(115,467,xp,10)
set.fillRect(192.4,468,xp,8)
set.fillRect(270,468,xp,8)
set.fillRect(356.3,468,0,8)
if (up_5 == 5){
	set.fillStyle = 'red'
	set.fillRect(356.3,468,xp,8)
}
set.drawImage(screen,-4,397)
if (up_5 == 4){
 set.fillStyle = 'grey'
 set.fillRect(345,405,55,55)
 set.fillStyle = 'white'
 set.fillText('lock',345,440)
} // и вот это
if (rx <= 110 &&  y + 80 > ry && y < ry + 170){ //проверка на проигрыш
   ry = ran(0,411);rx = 760;xp -= 6 //рандомайзер положений 
}
 if (score > 295 && score < 300){
 img.src = 'location/boss_battle.png'
 set.drawImage(img,0,0)
 x = -100
 rx = 500
 locationX = 0
 }
},1)
setInterval(function(){ //ещё один цикл
play1.src = 'sprite/утюг1.2.png' //анимация
set.drawImage(play1,x,y)         //утюга
if (score < 50){ //начало части отвечающей за скорость
rx -= 1
}
if (score >= 50){
	rx -= 3
}
if (score >= 100){
 rx -= 5
} //конец 
},2)
}
setInterval(function(){
score ++
},2000)