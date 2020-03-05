import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  public loginForm: FormGroup;

  constructor(private fb: FormBuilder, private router: Router,
    private route: ActivatedRoute) { }

  createLoginForm() {
    this.loginForm = this.fb.group({
      user: ['', Validators.required],
      password: ['', Validators.required],
    })
  }

  ngOnInit(){
    this.createLoginForm()
  }

  usuario = "amaka@gmail.com"
  contrasena = "12345Amaka";

  loginButton() {

    if ((this.loginForm.value.user === this.usuario) && (this.loginForm.value.password === this.contrasena)) {
      
      alert('cool');
      this.router.navigate(["/home"]);
      
    } else {
      alert('Usuario no encontrado, por favor ingresa un usuario válido o crea uno nuevo');
      this.loginForm.value.user = "";
      this.loginForm.value.password = "";
    }
  }

  newUserButton(){
    this.router.navigate(["/newUser"]);
  }

}
