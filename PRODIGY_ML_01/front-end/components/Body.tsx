'use client';

import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert';
import { Button } from '@/components/ui/button';
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage
} from '@/components/ui/form';
import { Input } from '@/components/ui/input';
import { PricePredictionRequest, QrGenerateResponse } from '@/utils/service';
import { zodResolver } from '@hookform/resolvers/zod';
import { AlertCircle } from 'lucide-react';
import { useForm } from 'react-hook-form';
import { Toaster } from 'react-hot-toast';
import * as z from 'zod';

import Component from '@/components/bar-chart';
import axios from 'axios';
import LoadingDots from './ui/loadingdots';
import { useState } from 'react';

const generateFormSchema = z.object({
  garageArea: z.string(),
  bedrooms: z.string(),
  totalSquareFootage: z.string(),
  totalArea: z.string(),
  bathrooms: z.string()
});

type GenerateFormValues = z.infer<typeof generateFormSchema>;

const Body = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<Error | null>(null);
  const [response, setResponse] = useState<QrGenerateResponse | null>(null);
  // eslint-disable-next-line no-unused-vars
  const [submittedURL, setSubmittedURL] = useState<string | null>(null);
  const [pricePrediction, setPricePrediction] = useState<number | null>(null)
  const [otherPrices, setOtherPrices] = useState<number[]>([])


  const form = useForm<GenerateFormValues>({
    resolver: zodResolver(generateFormSchema),
    mode: 'onChange',
  });


  const handleSubmit = async (values: GenerateFormValues) => {
    console.log('submit is called');
    setIsLoading(true);
    setResponse(null);

    try {
      const request: PricePredictionRequest = {
        garageArea: values.garageArea,
        bedrooms: values.bedrooms,
        totalSquareFootage: values.totalSquareFootage,
        totalArea: values.totalArea,
        bathrooms: values.bathrooms
      };
      const featuresArray = [
        parseInt(request.garageArea),
        parseInt(request.bedrooms),
        parseInt(request.totalSquareFootage),
        parseInt(request.totalArea),
        parseInt(request.bathrooms)
      ];
      const dataToSend = {
        features: [featuresArray]
      };

      const response = await axios.post('http://localhost:5000/predict', dataToSend);

      // Handle API errors.
      if (response.status !== 200) {
        throw new Error(`Failed to predict price: ${response.status}`);
      }

      const data = response.data;
      console.log(data);
      setPricePrediction(data.prediction[0])
      setOtherPrices(data.sale_prices)

    } catch (error) {
      console.log(error);
      if (error instanceof Error) {
        setError(error);
      }
    } finally {
      setIsLoading(false);
    }
  }


  return (
    <>
      <div className="flex justify-center items-center flex-col w-full lg:p-0 p-4 sm:mb-28 mb-0">
        <div className="max-w-6xl w-full grid grid-cols-1 md:grid-cols-2 gap-6 md:gap-12 mt-10">
          <div className="col-span-1">
            <h1 className="text-3xl font-bold mb-10">Predict House Price</h1>
            <Form {...form}>
              <form onSubmit={form.handleSubmit(handleSubmit)}>
                <div className="flex flex-col gap-4">
                  <FormField
                    control={form.control}
                    name="bathrooms"
                    render={({ field }) => (
                      <FormItem>
                        <FormLabel>Bathrooms</FormLabel>
                        <FormControl>
                          <Input placeholder="Number of bathrooms" {...field} />
                        </FormControl>
                        <FormMessage />
                      </FormItem>
                    )}
                  />
                  <FormField
                    control={form.control}
                    name="bedrooms"
                    render={({ field }) => (
                      <FormItem>
                        <FormLabel>Bedrooms</FormLabel>
                        <FormControl>
                          <Input placeholder="Number of bedrooms"  {...field} />
                        </FormControl>
                        <FormMessage />
                      </FormItem>
                    )}

                  />
                  <FormField
                    control={form.control}
                    name="totalArea"
                    render={({ field }) => (
                      <FormItem>
                        <FormLabel>Total Area</FormLabel>
                        <FormControl>
                          <Input placeholder="Total Area" {...field} />
                        </FormControl>
                        <FormMessage />
                      </FormItem>
                    )}
                  />
                  <FormField
                    control={form.control}
                    name="totalSquareFootage"
                    render={({ field }) => (
                      <FormItem>
                        <FormLabel>Total Square Footage</FormLabel>
                        <FormControl>
                          <Input placeholder="Total Square Footage" {...field} />
                        </FormControl>
                        <FormMessage />
                      </FormItem>
                    )}
                  />

                  <FormField
                    control={form.control}
                    name="garageArea"
                    render={({ field }) => (
                      <FormItem>
                        <FormLabel>Garage Area</FormLabel>
                        <FormControl>
                          <Input placeholder="Garage Area"  {...field} />
                        </FormControl>
                        <FormMessage />
                      </FormItem>
                    )}

                  />

                  <Button
                    type="submit"
                    disabled={isLoading}
                    className="inline-flex justify-center
                 max-w-[200px] mx-auto w-full"
                  >
                    {isLoading ? (
                      <LoadingDots color="white" />
                    ) : response ? (
                      '✨ Re-Predict'
                    ) : (
                      'Predict'
                    )}
                  </Button>

                  {error && (
                    <Alert variant="destructive">
                      <AlertCircle className="h-4 w-4" />
                      <AlertTitle>Error</AlertTitle>
                      <AlertDescription>{error.message}</AlertDescription>
                    </Alert>
                  )}
                </div>
              </form>
            </Form>
          </div>
          <div className="col-span-1 flex justify-center items-center">
            {pricePrediction &&
              <div>
                <h1 className="text-3xl font-bold mb-10">The average price of your house is:</h1>
                <div>
                  <p>

                    <div>
                      <p className="text-4xl font-bold text-center">
                        {/* get just  */}
                        {Math.floor(pricePrediction)}
                        <span className="text-3xl font-semibold">€</span>
                      </p>
                    </div>
                  </p>
                </div>
              </div>
            }
          </div>
        </div>
        <Toaster />
      </div>

      {
        otherPrices.length > 0 &&
        <Component prices={otherPrices} />
      }
    </>
  );
};

export default Body;
