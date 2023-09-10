import {AfterViewInit, Component, ElementRef, HostListener, ViewChild} from '@angular/core';
import {Store} from "@ngrx/store";
import {GlobalState} from "../shared/state/global-state";
import {Observable} from "rxjs";
import {Flow, Node} from "../core/model/Flow";
import {flow} from "../shared/state/flows/flows.selector";
import {CommonModule, NgFor, NgIf} from "@angular/common";

export interface Point {
  x: number;
  y: number;
}

@Component({
  standalone: true,
  selector: 'app-playground',
  templateUrl: './playground.component.html',
  styleUrls: ['./playground.component.css'],
  imports: [
    NgIf, CommonModule, NgFor
  ],
})
export class PlaygroundComponent implements AfterViewInit {
  @ViewChild('svgGrid', {read: ElementRef}) svgGrid!: ElementRef<SVGSVGElement>;
  flows$: Observable<Flow> = this.store.select(flow)
  isDraggingEvent = false;
  offsetX!: number;
  offsetY!: number;
  pointerX?: number = 0;
  pointerY?: number = 0;
  translateX: number = 0;
  translateY: number = 0;

  zoom:number=1

  constructor(private store: Store<GlobalState>) {
  }

  ngAfterViewInit(): void {
    this.computeCanvasOffset()
  }

  private computeCanvasOffset() {
    const pt = this.svgGrid.nativeElement.createSVGPoint();
    const offset = pt.matrixTransform(this.svgGrid.nativeElement.getScreenCTM()!)
    this.offsetX = offset.x
    this.offsetY = offset.y
  }

  @HostListener('document:pointerup', ['$event'])
  public upHandle(pointerEvent: PointerEvent) {
    pointerEvent.preventDefault()
    this.isDraggingEvent = false;
  }

  downHandleGrid(pointerEvent: PointerEvent) {
    pointerEvent.preventDefault();
    this.isDraggingEvent = true;
    this.pointerX = pointerEvent.clientX - this.offsetX
    this.pointerY = pointerEvent.clientY - this.offsetY
  }

  moveHandleGrid(pointerEvent: PointerEvent) {
    pointerEvent.preventDefault();
    if (this.isDraggingEvent) {
      const vectorX = (pointerEvent.clientX - this.offsetX) - this.pointerX!
      const vectorY = (pointerEvent.clientY - this.offsetY) - this.pointerY!
      this.translateX = this.translateX + vectorX
      this.translateY = this.translateY + vectorY
      this.pointerX = pointerEvent.clientX- this.offsetX
      this.pointerY = pointerEvent.clientY- this.offsetY
    }
  }

  clickHandleGrid(pointerEvent: MouseEvent) {
    pointerEvent.preventDefault();
  }
  translate() {
    return 'translate(' + this.translateX + ', '+this.translateY+') scale('+this.zoom+','+this.zoom+')'
  }


  nodeType(node: Node) {
    if (node.type == 'PROCESS_GROUP') {
      return 'G';
    }
    if (node.type == 'PROCESSOR') {
      return 'P';
    }
    if (node.type == 'REMOTE_PROCESS_GROUP') {
      return 'RG';
    }
    if (node.type == 'FUNNEL') {
      return 'F';
    }
    if (node.type == 'INPUT_PORT') {
      return 'I';
    }
    if (node.type == 'OUTPUT_PORT') {
      return 'O';
    }
    return '?';
  }

  wheelHandleGrid(wheelEvent: WheelEvent){
    wheelEvent.preventDefault();
    console.log(wheelEvent.deltaY)
    this.zoom = wheelEvent.deltaY>0 ? this.zoom - 0.1 : this.zoom+ 0.1
  }

  resetView() {
    this.translateX=0
    this.translateY=0
    this.zoom=1
  }
}
