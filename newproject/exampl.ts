export interface CarSpecs {
    gasoline: string
    steering: string
    capacity: string
  }
  
  export interface CarCardTypes {
    id?: number
    slug?: string
    in_wishlist: boolean
    name: string
    car_type: string
    image: string
    specs: CarSpecs
    price: string
    discount?: string | null
  }
  
  export interface CarDetails extends Omit<CarCardTypes, 'image'> {
    description: string
    images: Array<string>
    rating: {
      average: number
      total: number
    }
  }
  
  // params = car_id
  export interface CarReviews {
    page: number
    total: number
    data: CarReview[]
  }
  
  export interface CarReview {
    id: string
    date: Date
    rating: number
    review: string
    user: {
      avatar: string
      name: string
      bio: string
    }
  }
  
  export type Recommended = CarCardTypes[]
  export type Recent = CarCardTypes[]