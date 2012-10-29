jQuery(function(){
	jQuery('.rundata_type').change(function(){
		AddProblem.changeRundataType( this );
	});
	jQuery('#add_rundata').click(function(){
		AddProblem.addRunDataType();
		return false;
	});
	jQuery('#submit_problem').click(function(){
		return jdmd_widget.validate_and_error_all(jQuery(this).closest('form').get(0));
	});
});
var AddProblem={};
AddProblem.changeRundataType = function(o){
	switch( o.value ){
	case 'input':
		jQuery(o).closest('.rundata').find('.rundata_input_block').css('display','block');
		jQuery(o).closest('.rundata').find('.rundata_upload_block').css('display','none');
		break;
	case 'upload':
		jQuery(o).closest('.rundata').find('.rundata_input_block').css('display','none');
		jQuery(o).closest('.rundata').find('.rundata_upload_block').css('display','block');
		break;
	}
}
var rundata_num = 0;
AddProblem.addRunDataType = function(){
	var sampleObj = jQuery('.rundata_sample').get(0);
	var oriCode = sampleObj.outerHTML ;
	var nCode = oriCode.replace(/{num}/g,++rundata_num);
	
	var lastRunData = jQuery('.rundata').last() ;
	var nObj = lastRunData.after( nCode ).next();
	nObj.removeClass('rundata_sample');
	
	nObj.find('.rundata_type').change(function(){
		AddProblem.changeRundataType( this );
	});
	nObj.find('.rundata_type').get(0).checked = true;
	jQuery( nObj.find('.rundata_type').get(0) ).change();
}
