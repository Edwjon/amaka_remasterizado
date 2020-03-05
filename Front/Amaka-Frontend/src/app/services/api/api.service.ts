import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor( private api:HttpClient) {}

  apiGET(path){
    return this.api.get( path )
  }
  
  apiGETone(path, id){
    return this.api.get( path+'/'+id )
  }

  apiPOST(path, data){
    return this.api.post( path, data )
  }
}
