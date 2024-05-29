 const checkPermission = () => {
    if (!('serviceWorker' in navigator))
        throw new Error('Service worker permission not supported!')
   
    if(!('Notification' in window)){
      throw new Error('No support for notofication API')
    }
 }

 const registerSW = async () => {
    const registration = await navigator.serviceWorker.register('/sw.js')
    return registration
 }

 const requestNotificationPermission = async () => {
    const permission = await Notification.requestPermission()
    if (permission != 'granted'){
      throw new Error('Notification permission not granted')
    }else{
      new Notification('Test')
    }
    
 }
 checkPermission()
 registerSW()
 requestNotificationPermission()