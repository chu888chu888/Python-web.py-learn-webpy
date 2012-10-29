jQuery(function(){
	jQuery('.rundata_type').change(function(){
		AddProblem.changeRundataType( this );
	});
	jQuery('#add_rundata').click(function(){
		AddProblem.addRunDataType();
		return false;
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
}
