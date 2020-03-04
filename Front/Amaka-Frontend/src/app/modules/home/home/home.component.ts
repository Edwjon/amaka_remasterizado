import { Component, OnInit } from '@angular/core';
import { ProductsService } from 'src/app/services/products/products.service';
import { ActivatedRoute, Router } from '@angular/router';
import { SidebarService } from 'src/app/services/sideBar/side-bar.service';
import { Product } from 'src/app/models/product';
import { i18nMetaToDocStmt } from '@angular/compiler/src/render3/view/i18n/meta';

// export interface product {
//   img: string;
//   name: string;
//   // selected: boolean;
//   type: string;
//   price: number;
// }

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  productsAvailable = [];

  constructor(private route: ActivatedRoute,
    private router: Router, private productService: ProductsService,
    private sideBarSV: SidebarService) { 

      // this.productsAvailable = productService.getProducts();s
    }

    seleccionado(product){
      const id = product.Id;
      this.router.navigate(["/home/product-details", product.Id])
    }

    toggleSideBar() {
      this.sideBarSV.toggleShoppingCartStatus();
    }
//   products: product[] = [{
//     img: 'https://http2.mlstatic.com/mega-curso-elaboracion-de-quesos-casero-productos-lacteos-D_NQ_NP_766893-MLV31252305217_062019-F.jpg',
//     name: 'hola',
//     type: 'queso',
//     price: 123,
//   }, 
// {
//   img: 'https://http2.mlstatic.com/mega-curso-elaboracion-de-quesos-casero-productos-lacteos-D_NQ_NP_766893-MLV31252305217_062019-F.jpg',
//     name: 'hola',
//     type: 'queso',
//     price: 123,
// }, {
//   img: 'https://http2.mlstatic.com/mega-curso-elaboracion-de-quesos-casero-productos-lacteos-D_NQ_NP_766893-MLV31252305217_062019-F.jpg',
//     name: 'hola',
//     type: 'queso',
//     price: 123,
// }, {
//   img: 'https://http2.mlstatic.com/mega-curso-elaboracion-de-quesos-casero-productos-lacteos-D_NQ_NP_766893-MLV31252305217_062019-F.jpg',
//     name: 'hola',
//     type: 'queso',
//     price: 123,
// }, {
//   img: 'https://http2.mlstatic.com/mega-curso-elaboracion-de-quesos-casero-productos-lacteos-D_NQ_NP_766893-MLV31252305217_062019-F.jpg',
//     name: 'hola',
//     type: 'queso',
//     price: 123,
// }];

  ngOnInit() {
    this.productService.sendGetRequest().subscribe((data: Product[])=>{
      // console.log(data);
      this.productsAvailable = data;
      console.log("aqui ta:", this.productsAvailable);
      
    })  
  }

}

