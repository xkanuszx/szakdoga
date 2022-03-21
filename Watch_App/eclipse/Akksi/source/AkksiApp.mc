import Toybox.Application;

class AkksiApp extends Application.AppBase {

    function initialize() {
        AppBase.initialize();
    }

    // onStart() is called on application start up
    function onStart(state as Dictionary?) as Void {
    }

    // onStop() is called when your application is exiting
    function onStop(state as Dictionary?) as Void {
    }

    // Return the initial view of your application here
    function getInitialView() as Array<Views or InputDelegates>? {
        return [ new AkksiView() ] as Array<Views or InputDelegates>;
    }

}

function getApp() as AkksiApp {
    return Application.getApp() as AkksiApp;
}