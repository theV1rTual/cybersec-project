import { CartService } from './../../services/cart/cart.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.scss']
})
export class CartComponent implements OnInit {

  cartProducts: any[] = []
  cartEmpty:boolean = true
  totalPrice: number = 0

  constructor(private cartService: CartService) { }

  ngOnInit(): void {
    this.getCartProducts()
    this.getTotalPrice()
  }

  getCartProducts() {
    this.cartProducts = this.cartService.cartProducts
    if(this.cartProducts.length > 0) {
      this.cartEmpty = false
    }
  }

  getTotalPrice() {
    for(let i = 0; i < this.cartProducts.length; i++) {
      this.totalPrice += this.cartProducts[i].price
    }
  }

}
