import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ProductsService {

  selectedCategory: string = ''

  constructor(private http: HttpClient) { }

  getProducts() {
    return this.http.get('https://fakestoreapi.com/products/category/' + this.selectedCategory)
  }
}
