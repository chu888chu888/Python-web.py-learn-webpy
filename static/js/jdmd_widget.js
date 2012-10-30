jdmd_widget = {};
jdmd_widget.init = function(){
	jQuery('.jdmd_input').change(function(){
		jdmd_widget.validate_and_error( this );
	});
}
jdmd_widget.validate_and_error = function(o){
	var rst = jdmd_widget.validate(o);
	if( true == rst.result ){
		jdmd_widget.clearError(o);
		return true;
	}else{
		jdmd_widget.showError(o,rst.msg);
		return false;
	}
}
jdmd_widget.validate = function(o){
	var validate_list = jQuery(o).attr('validate');
	if( undefined == validate_list ){
		return {
			result:true,
			msg:'xxx'
		};
	}
	validate_list = validate_list.split(' ');
	
	var val = jQuery(o).val();
	
	var i;
	var rtn = {
		result:true,
		msg:''
	};
	for(i in validate_list){
		var v = validate_list[i];
		switch(v){
		case 'notempty':
			if( '' == val ){
				rtn.result = false;
				rtn.msg += '内容不能为空;';
			}
			break;
		case 'int':
			if( ! val.match(/^[0-9]+$/) ){
				rtn.result = false;
				rtn.msg += '内容必须为数字;';
			}
			break;
		}
	}
	
	return rtn;
}
jdmd_widget.clearError=function(o){
	jQuery(o).parent().find('.jdmd_widget_validate_error').remove();
}
jdmd_widget.showError=function(o,msg){
	jQuery(o).parent().append("<div class='jdmd_widget_validate_error'><div class='icon'></div><div class='content'>"+msg+"</div></div>");
}
jdmd_widget.validate_and_error_all = function(o){
	var rtn = true;
	jQuery(o).find('.jdmd_input').each(function(){
		var v = jdmd_widget.validate_and_error(this);
		if( false == v ){
			rtn = false;
		}
	});
	return rtn;
}

if( jQuery != undefined ){
	jQuery(function(){
		jdmd_widget.init();
	});
}
