const copyBtn = document.querySelector('.copy')
const shortUrl = document.querySelector('#short-url')
const longUrl = document.querySelector('#long-url')
const qrBtn = document.querySelector('.qrBtn')
const qr = document.querySelector('.qrcode')

if (copyBtn) {
    copyBtn.addEventListener('click', copyUrl)
}

if (qrBtn) {
    qrBtn.addEventListener('click', showCode)
}

function showCode() {
    if (qr.classList.contains('show')) return
    qr.classList.add('show')
}

async function copyUrl() {
    const text = getUrl()
    console.log(text)
    try {
        await navigator.clipboard.writeText(text)
    } catch(err) {
        console.error("Couldnt Copy text:", err)
    }
}

function getUrl() {
    if (shortUrl) {
        return shortUrl.textContent;
    } else if (longUrl){
        return longUrl.textContent
    }
}
