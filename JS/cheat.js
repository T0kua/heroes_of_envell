var up_5 = 4
document.addEventListener('keydown',function(e){
 if (e.which === 49){
  xp = 30
 }
 if (e.which === 50){
	score += 50
	locationX = 0
 }
 if (e.which === 70){
 x = 30
 final = true
 }
 if (e.which === 8){
 	up_5 = 5
 }
})