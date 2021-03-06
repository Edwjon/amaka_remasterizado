import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Product } from 'src/app/models/product';
import { ProductsService } from 'src/app/services/products/products.service';
import { SidebarService } from 'src/app/services/sideBar/side-bar.service';
import { ShoppingCartService } from 'src/app/services/shoppingCart/shopping-cart.service';

@Component({
  selector: 'app-product-details',
  templateUrl: './product-details.component.html',
  styleUrls: ['./product-details.component.scss']
})
export class ProductDetailsComponent implements OnInit {

  
  product
  selectedProduct
  productId

  // PRODUCT: Product[] = [
  //   {
  //     name: "holi",
  //     size: "grande",
  //     price: 10,
  //   }
  // ]
  public productsQuantityForm: FormGroup;

  constructor(private route: ActivatedRoute,
    private router: Router, private fb: FormBuilder,
    private productService: ProductsService, private sideBarSV: SidebarService, private shoppingCartSV: ShoppingCartService) { }

  createProductsQuantityForm() {
    this.productsQuantityForm = this.fb.group({
      quantity: ['', [Validators.required, Validators.min(1)]],
    });
  }

  toggleSideBar() {
    this.sideBarSV.toggleShoppingCartStatus();
  }

  addProduct (){
    this.route.paramMap.subscribe( params => {
      this.shoppingCartSV.addProduct(params.get('id'), this.productsQuantityForm.value.quantity);
    })
    
  }

  ngOnInit() {
      this.route.paramMap.subscribe( params => {
      // this.productId = this.route.snapshot.paramMap.get('id');
      this.selectedProduct = this.productService.getProduct(params.get('id'));
      // console.log(this.productId);
      console.log("jepa:", this.selectedProduct);
      
    })
    

    this.createProductsQuantityForm();

  }

}
