import { getStorageItem, setStorageItem } from './utils.js';
let store = getStorageItem('store');
const setupStore = (products) => {
    store = products.map((product) => {
        console.log(product);
        const {
            id,
            fields: { featured, name, price, company, colors, image: img},
        } = product;
        // const image = img[0].thumbnails.large.url;
        console.log("img ====", img)
        const image = img[0].url;
        return { id, featured, name, price, company, colors, image };
    });
    setStorageItem('store', store);
};

const findProduct = (id) => {
    let product = store.find((product) => product.id === id);
    return product;
};

export { store, setupStore, findProduct };