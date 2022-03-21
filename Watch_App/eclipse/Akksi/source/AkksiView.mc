import Toybox.WatchUi;
import Toybox.System;
import Toybox.Math;
import Toybox.FitContributor;

class AkksiView extends WatchUi.SimpleDataField {
	const BATT_FIELD_ID = 0;
	hidden var batt_field;
	hidden var old_batt;
   
    function initialize() {
        SimpleDataField.initialize();
        label = "Myakksi";
        
        batt_field = createField(
				"Myakksi2",
				BATT_FIELD_ID,
				FitContributor.DATA_TYPE_UINT8,
				{:mesgType=>FitContributor.MESG_TYPE_RECORD, :units=>"%"});
    }

    // The given info object contains all the current workout
    // information. Calculate a value and return it in this method.
    // Note that compute() and onUpdate() are asynchronous, and there is no
    // guarantee that compute() will be called before onUpdate().
    function compute(info as Activity.Info) as Numeric or Duration or String or Null {
        var stats = System.getSystemStats();
		var new_batt = Math.round(stats.battery).toNumber();
		if (new_batt != old_batt) {
			batt_field.setData(new_batt);
			old_batt = new_batt;
		}
		return stats.battery.format("%0.1f");
    }

}