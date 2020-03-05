import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './modules/home/home/home.component';
import { CommonNavigationComponent } from './navigation/common-navigation/common-navigation.component';
import { AdminNavigationComponent } from './navigation/admin-navigation/admin-navigation.component';
import { LoginComponent } from './modules/home/login/login.component';
import { NewUserComponent } from './modules/home/new-user/new-user.component';
// import { ShowDataComponent } from './show-data/show-data.component';
// import { PagenotfoundComponent } from './pagenotfound/pagenotfound.component';


const routes: Routes = [
  {
    path: '',
    redirectTo: '/login',
    pathMatch: 'full',
  },
  {
    path: '',
    component: CommonNavigationComponent,
    children: [
      {
        path: 'home',
        loadChildren: () => import('./modules/home/home.module').then(m => m.HomeModule)
      },
      {
        path: 'login',
        component: LoginComponent
      },
      {
        path: 'newUser',
        component: NewUserComponent
      },
    ]
  },
  {
    path: '',
    component: AdminNavigationComponent,
    children: [
      {
        path: 'admin',
        loadChildren: () => import('./modules/admin/admin.module').then (m => m.AdminModule)
      },
    ]
  },
  // {
  //   path: '',
  //   redirectTo: '/vacationBuilder',
  //   pathMatch: 'full',
  // },
  // {
  //   path: '',
  //   component: VacationBuilderNavigationComponent,
  //   children: [
  //     {
  //       path: 'vacationBuilder',
  //       loadChildren: () => import('./modules/vacationBuilder/vacation-builder.module').then (m => m.VacationBuilderModule)
  //     },
  //   ]
  // },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
