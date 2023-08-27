import {Injectable} from "@angular/core";
import {HttpClient, HttpHeaders, HttpResponse} from "@angular/common/http";
import {CreateProjectRequest, Project} from "../model/Project";
import {Observable} from "rxjs";
import {config} from "../../../config";

@Injectable({
  providedIn: 'root'
})
export class BackendService {
  private url = config.backendUrl;
  private header = new HttpHeaders({'Content-Type': 'application/json'})

  constructor(private http: HttpClient) {
  }

  public addProject(project: CreateProjectRequest): Observable<HttpResponse<any>> {
    return this.http.post(`${this.url}/projects`, project, {
      headers: this.header,
      observe: 'response'
    })
  }

  public getAll(): Observable<HttpResponse<Project[]>> {
    return this.http.get<[Project]>(`${this.url}/projects`, {
      observe: 'response'
    })
  }

  public deleteProject(project_id: string): Observable<HttpResponse<any>>  {
    return this.http.delete(`${this.url}/projects/${project_id}`,{
      headers: this.header,
      observe: 'response'
    })
  }
}
