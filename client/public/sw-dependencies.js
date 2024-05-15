 const checkPermission = () => {
    if (!('serviceWorker' in navigator))
        throw new Error('Service worker permission not supported!')
 }

 const registerSW = async () => {
    const registration = await navigator.serviceWorker.register('/sw.js')
    return registration
 }
 checkPermission()
 registerSW()