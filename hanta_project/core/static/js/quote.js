
document.addEventListener('DOMContentLoaded', () => {


    const category = "happiness"
    const apiKey = "kiU61swQc5r/Fnk51EBrjw==o4whGWVgvuvo3S2u"

    const fecthQuoate = async () => {
        const response = await fetch(`https://api.api-ninjas.com/v1/quotes?category=${category}&X-Api-Key=${apiKey}`);
        const quote = await response.json();
        console.log(quote)
        insertQuoate(quote[0]);
    }

    fecthQuoate();


    const insertQuoate = ({ quote, author }) => {

        const container = document.querySelector('.quote')
        container.innerHTML = `
        <p class="p-2 fst-italic ">"${quote}" - <span class="fw-bolder">${author}</span>
        </p>
        `

    }
})
