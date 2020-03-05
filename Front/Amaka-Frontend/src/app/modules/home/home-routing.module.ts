import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { ProductDetailsComponent } from './product-details/product-details.component';
import { LoginComponent } from './login/login.component';
import { NewUserComponent } from './new-user/new-user.component';


const routes: Routes = [ {
  path: '',
  redirectTo: '/home/login',
  pathMatch: 'full'
},
  {
    path: '',
    children:[
      {
        path: 'login',
        component: LoginComponent
      },
      {
        path: 'newUser',
        component: NewUserComponent
      },
      {
        path: 'home',
        component: HomeComponent
      },
      {
        path: 'product-details/:id',
        component: ProductDetailsComponent
      },
    ]
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class HomeRoutingModule { }
