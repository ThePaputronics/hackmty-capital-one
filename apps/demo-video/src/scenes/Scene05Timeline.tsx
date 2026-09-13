import React from 'react';
import { interpolate, useCurrentFrame } from 'remotion';
import { theme } from '../theme';
import { DecisionBadge } from '../components/DecisionBadge';
import simulationData from '../data/simulation.json';

export const Scene05Timeline: React.FC = () => {
  const frame = useCurrentFrame();

  // Progress through 30 days over 420 frames
  const currentDay = Math.min(30, Math.floor(interpolate(frame, [0, 380], [1, 30], { extrapolateRight: 'clamp' })));
  const evaluatedCount = Math.floor(interpolate(frame, [0, 380], [0, simulationData.total], { extrapolateRight: 'clamp' }));

  // Revealed items
  const visibleCount = Math.min(10, Math.floor(interpolate(frame, [0, 350], [1, 10], { extrapolateRight: 'clamp' })));
  const items = simulationData.feed_sample.slice(0, visibleCount);

  return (
    <div
      style={{
        flex: 1,
        backgroundColor: theme.colors.bg,
        display: 'flex',
        flexDirection: 'column',
        padding: '60px 100px',
        justifyContent: 'space-between',
      }}
    >
      {/* Header bar */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-end', borderBottom: `1px solid ${theme.colors.surfaceBorder}`, paddingBottom: '20px' }}>
        <div>
          <span style={{ color: theme.colors.accent, fontFamily: theme.fonts.mono, fontSize: '14px', letterSpacing: '2px', textTransform: 'uppercase' }}>
            Live Stream Replay · Seed 42
          </span>
          <h2 style={{ color: '#fff', fontFamily: theme.fonts.serif, fontSize: '38px', margin: '6px 0 0 0' }}>
            Simulación Continua de 30 Días
          </h2>
        </div>
        <div style={{ display: 'flex', gap: '30px' }}>
          <div style={{ textAlign: 'right' }}>
            <div style={{ color: theme.colors.textMuted, fontSize: '13px', fontFamily: theme.fonts.mono }}>RELOJ SIMULADO</div>
            <div style={{ color: theme.colors.accentLight, fontSize: '28px', fontFamily: theme.fonts.mono, fontWeight: 700 }}>
              Día {currentDay} <span style={{ fontSize: '16px', color: '#888' }}>/ 30</span>
            </div>
          </div>
          <div style={{ textAlign: 'right' }}>
            <div style={{ color: theme.colors.textMuted, fontSize: '13px', fontFamily: theme.fonts.mono }}>TRANSACCIONES EVALUADAS</div>
            <div style={{ color: '#fff', fontSize: '28px', fontFamily: theme.fonts.mono, fontWeight: 700 }}>
              {evaluatedCount}
            </div>
          </div>
        </div>
      </div>

      {/* Feed table */}
      <div
        style={{
          flex: 1,
          margin: '25px 0',
          backgroundColor: theme.colors.surface,
          border: `1px solid ${theme.colors.surfaceBorder}`,
          borderRadius: '12px',
          overflow: 'hidden',
          display: 'flex',
          flexDirection: 'column',
        }}
      >
        <div
          style={{
            display: 'grid',
            gridTemplateColumns: '80px 180px 160px 1fr 140px',
            padding: '14px 24px',
            borderBottom: `1px solid ${theme.colors.surfaceBorder}`,
            color: theme.colors.textMuted,
            fontFamily: theme.fonts.mono,
            fontSize: '12px',
            textTransform: 'uppercase',
            letterSpacing: '1px',
          }}
        >
          <div>Día</div>
          <div>Ordenante</div>
          <div>Monto</div>
          <div>Destinatario CLABE</div>
          <div style={{ textAlign: 'right' }}>Decisión</div>
        </div>

        <div style={{ flex: 1, display: 'flex', flexDirection: 'column' }}>
          {items.map((it: any) => (
            <div
              key={it.id}
              style={{
                display: 'grid',
                gridTemplateColumns: '80px 180px 160px 1fr 140px',
                padding: '12px 24px',
                borderBottom: `1px solid ${theme.colors.border}`,
                alignItems: 'center',
                fontFamily: theme.fonts.sans,
                fontSize: '15px',
              }}
            >
              <div style={{ color: theme.colors.textMuted, fontFamily: theme.fonts.mono }}>D{it.day}</div>
              <div style={{ color: theme.colors.textPrimary, fontFamily: theme.fonts.mono }}>{it.payer_id}</div>
              <div style={{ color: '#fff', fontWeight: 600, fontFamily: theme.fonts.mono }}>
                ${it.amount.toLocaleString('es-MX', { minimumFractionDigits: 2 })}
              </div>
              <div style={{ color: theme.colors.textSecondary, fontFamily: theme.fonts.mono, fontSize: '13px' }}>
                {it.destination_clabe} ({it.destination_institution})
              </div>
              <div style={{ textAlign: 'right' }}>
                <DecisionBadge decision={it.decision} size="sm" />
              </div>
            </div>
          ))}
        </div>
      </div>

      <div style={{ color: theme.colors.textMuted, fontSize: '14px', fontFamily: theme.fonts.sans }}>
        Cada transferencia es evaluada contra la línea base histórica del ordenante hasta la fecha propuesta (<code>as_of</code>). Cero sesgo hacia el futuro.
      </div>
    </div>
  );
};
