var w = window.screen.availWidth;
if(w > 1000){
    let bg = document.querySelector('.BG')
    let text = document.querySelector('.text')
	window.addEventListener('mousemove', function(e) {
	    let x = e.clientX / window.innerWidth;
	    let y = e.clientY / window.innerHeight;
	    bg.style.transform = 'translate(+' + x * 15 + 'px, +' + y * 15 + 'px)';
	    text.style.transform = 'translate(-' + x * 15 + 'px, -' + y * 15 + 'px)';
	});
};
