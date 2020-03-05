import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-new-user',
  templateUrl: './new-user.component.html',
  styleUrls: ['./new-user.component.scss']
})
export class NewUserComponent implements OnInit {

  public userForm: FormGroup;

  constructor(private fb: FormBuilder, private router: Router,
    private route: ActivatedRoute) { }

  createUserForm() {
    this.userForm = this.fb.group({
      name: ['', Validators.required],
      lastName: ['', Validators.required],
      email: ['', Validators.required],
      password: ['', Validators.required],
    });
  }

  saveUser(){
    this.router.navigate(["/login"]);
  }

  backToLogin(){
    this.router.navigate(["/login"]);
  }

  ngOnInit(){
    this.createUserForm();
  }

}
