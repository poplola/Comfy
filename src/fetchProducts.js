import { allProductsUrl } from './utils.js';

const fetchProducts = async () => {
    const response = await fetch(allProductsUrl).catch((err) => console.log(err));
    if (response) {
        console.log("==== response =====",response);
        // console.log("===== response.json() =====",response.json());
        return response.json();
    }
    return response;
};

export default fetchProducts;