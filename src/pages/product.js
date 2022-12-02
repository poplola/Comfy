// global imports
import '../toggleSidebar.js';
import '../cart/toggleCart.js';
import '../cart/setupCart.js';

//specific
import { addToCart } from '../cart/setupCart.js';
import { singleProductUrl, getElement, formatPrice } from '../utils.js';

// selections
const loading = getElement('.page-loading');
const centerDOM = getElement('.single-product-center');
const pageTitleDOM = getElement('.page-hero-title');
const imgDOM = getElement('.single-product-img');
const titleDOM = getElement('.single-product-title');
const companyDOM = getElement('.single-product-company');
const priceDOM = getElement('.single-product-price');
const colorDOM = getElement('.single-product-colors');
const descDOM = getElement('.single-product-desc');
const cartBtn = getElement('.addToCartBtn');

// cart product
let productID;

// show product when page loads
window.addEventListener('DOMContentLoaded', async function () {
    const urlID = window.location.search;

    try {
        console.log(`${singleProductUrl}${urlID}`)
        const response = await this.fetch(`${singleProductUrl}${urlID}`);
        
        if (response.status >= 200 && response.status <= 299) {
            const product = await response.json();

            console.log("product", product)
            // grab data
            const [{ id, fields }] = product;

            // console.log(id)
            // console.log(fields)
            productID = id;
            // console.log(productID)
            

            // console.log(fields)
            // const { name, company, price, colors, description } = fields;
            const { company, colors, price, name, description } = fields;
            // const image = fields.image[0].thumbnails.large.url;
            const image = fields.image[0].url;
            // set values

            document.title = `${name.toUpperCase()} | Comfy`;
            pageTitleDOM.textContent = `Home / ${name}`;
            imgDOM.src = image;
            titleDOM.textContent = name;
            companyDOM.textContent = `by ${company}`;
            priceDOM.textContent = formatPrice(price);
            descDOM.textContent = description;
            colors.forEach((color) => {
                const span = document.createElement('span');
                span.classList.add('product-color');
                span.style.backgroundColor = `${color}`;
                colorDOM.appendChild(span);
            });
        } else {
            console.log(response.status, response.statusText);
            centerDOM.innerHTML = `
                <div>
                    <h3 class="error">sorry, something went wrong</h3>
                    <a href="index.html" class="btn">back home</a>
                </div>
            `;
        }
    } catch (error) {
        console.log(error);
    }

    loading.style.display = 'none';
});

cartBtn.addEventListener('click', function () {
    addToCart(productID);
});