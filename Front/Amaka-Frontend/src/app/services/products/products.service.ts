import { Injectable } from '@angular/core';
import { Product } from 'src/app/models/product';
import { HttpClient, HttpErrorResponse, HttpParams } from "@angular/common/http";
import { Observable } from 'rxjs/internal/Observable';

// import {  throwError } from 'rxjs';
// import { retry, catchError } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})

export class ProductsService {

  products = [];

  private REST_API_SERVER = "http://localhost:3000/products";

  // products: Product[] = [{
  //   Id: '123ab',
  //   img: 'https://http2.mlstatic.com/mega-curso-elaboracion-de-quesos-casero-productos-lacteos-D_NQ_NP_766893-MLV31252305217_062019-F.jpg',
  //   name: 'quesote',
  //   // size: 'grande',
  //   price: 12,
  // },
  // {
  //   Id: '456cd',
  //   img: 'https://http2.mlstatic.com/mega-curso-elaboracion-de-quesos-casero-productos-lacteos-D_NQ_NP_766893-MLV31252305217_062019-F.jpg',
  //   name: 'quesito',
  //   // size: 'peque',
  //   price: 1233,
  // },
  // {
  //   Id: '789ef',
  //   img: 'https://http2.mlstatic.com/mega-curso-elaboracion-de-quesos-casero-productos-lacteos-D_NQ_NP_766893-MLV31252305217_062019-F.jpg',
  //   name: 'queso',
  //   // size: 'mediano',
  //   price: 1243,
  // },
  // {
  //   Id: '101gh',
  //   img: 'https://http2.mlstatic.com/mega-curso-elaboracion-de-quesos-casero-productos-lacteos-D_NQ_NP_766893-MLV31252305217_062019-F.jpg',
  //   name: 'quesosote',
  //   // size: 'gigante',
  //   price: 1253,
  // },
  // {
  //   Id: '102ij',
  //   img: 'https://http2.mlstatic.com/mega-curso-elaboracion-de-quesos-casero-productos-lacteos-D_NQ_NP_766893-MLV31252305217_062019-F.jpg',
  //   name: 'mini quesi',
  //   // size: 'chiquitin',
  //   price: 1423,
  // }];


  constructor(private httpClient: HttpClient) {
    this.sendGetRequest().subscribe((data: Product[]) => {
      console.log("qloq aqui", data);

      this.products = data;
    })
  }

  public sendGetRequest() {

    return this.httpClient.get(this.REST_API_SERVER);
  }

  //private products: Product[] = this.sendGetRequest();

  // getProducts() {
  //   return this.products;
  // }

  getProduct(id) {

    // console.log("holita:", this.products.find(product => (product.Id).toString() === id));
    // let productSelected = this.products.find(product => (product.Id).toString() === id);

    // console.log("jasdjash", productSelected.name);
    console.log(`${this.REST_API_SERVER}/${id}`);
    // return this.httpClient.get(`${this.REST_API_SERVER}/?Id:${id}`) as Observable<Product>
    return this.httpClient.get(this.REST_API_SERVER, {params: new HttpParams({fromString: `Id=${id}`}), observe: "response"})

    // return productSelected;
    // return this.products.find(product => product.Id === id);
  }

}
