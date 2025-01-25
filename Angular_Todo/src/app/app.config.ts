import { ApplicationConfig } from "@angular/core";
import { provideRouter, withComponentInputBinding, withRouterConfig } from "@angular/router";
import { routes } from "./app.route";

export const appConfig : ApplicationConfig = {
    providers : [
        provideRouter(routes, withComponentInputBinding(), withRouterConfig(
            {
                paramsInheritanceStrategy: 'always',
            }
        )),
    ],
}