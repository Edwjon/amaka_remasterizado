var faker = require('faker');

var database = { products: []};

for (var i = 1; i<= 10; i++) {
  database.products.push({
    Id: i,
    img: "https://source.unsplash.com/1600x900/?product",
    name: faker.commerce.productName(),
    // description: faker.lorem.sentences(),
    price: faker.commerce.price(),
    // quantity: faker.random.number()
  });
}

console.log(JSON.stringify(database));