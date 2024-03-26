export interface PricePredictionRequest {
  garageArea: string;
  bedrooms: string;
  totalSquareFootage: string;
  totalArea: string;
  bathrooms: string;
}

export interface QrGenerateResponse {
  image_url: string;
  model_latency_ms: number;
  id: string;
}
