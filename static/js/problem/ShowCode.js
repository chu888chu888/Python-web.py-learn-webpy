var ShowCode={};
ShowCode.init = function(){
	var language = this.analyseLanguage();
	var preObj = jQuery('pre');
	preObj.addClass('sh_'+language);
	
	try{
		loadStyle();
	}catch(e){
	}
	sh_highlightDocument('/static/shjs-0.6/lang/', '.js');
}
ShowCode.analyseLanguage=function(){
	return 'cpp';
}

jQuery(function(){
	ShowCode.init();
});
