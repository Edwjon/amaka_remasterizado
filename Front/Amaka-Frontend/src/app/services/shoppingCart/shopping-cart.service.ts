import { Injectable } from '@angular/core';
import { Product, ShoppingProduct } from 'src/app/models/product';
import { ProductsService } from '../products/products.service';
import { BehaviorSubject } from 'rxjs';
import { SidebarService } from '../sideBar/side-bar.service';

@Injectable({
  providedIn: 'root'
})
export class ShoppingCartService {

  shoppingCartProducts: ShoppingProduct[] = [];
  shoppingCartProducts$ = new BehaviorSubject<ShoppingProduct[]>(null);
  totalCart$ = new BehaviorSubject<number>(0);



  constructor(private productService: ProductsService, private sideBarSV: SidebarService) { }

  addProduct(product, quantity) {
    let alreadyInCart = this.shoppingCartProducts.find( e => e.Id === product.Id);
    if( alreadyInCart ){
      alreadyInCart.quantity = alreadyInCart.quantity + quantity
    } else {
      //... => spread operator => toma todos los valores del objeto
      let productToAdd = { ...product, quantity }
      this.shoppingCartProducts.push(productToAdd);
    }
    
    this.updateShoppingCart();
    this.sideBarSV.toggleShoppingCartStatus();
  }

  updateShoppingCart(){
    this.shoppingCartProducts$.next(this.shoppingCartProducts);

    let total = this.shoppingCartProducts.reduce( function (accumulator, product: ShoppingProduct) {
      return accumulator + (product.price * product.quantity) ;
    }, 0);
    this.totalCart$.next(total);

    // Aqui mandas lo que sea a la BD
  }

  getProduct() {
  }

  deleteProduct() {
  }

}
